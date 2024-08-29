from __future__ import annotations

import logging
import re

logger = logging.getLogger(__name__)
global_responses = {
    '400': {'$ref': '#/components/responses/validation-error'},
    '4XX': {'$ref': '#/components/responses/generic-error'},
    '5XX': {'$ref': '#/components/responses/generic-error'},
}


def sorted_dict(d: dict) -> dict:
    return {k: v for k, v in sorted(d.items(), key=lambda e: e[0])}


class GSMTasksSchemaPlugin:
    async def process_mapping(self, model: dict, _: object, _1: object) -> dict:
        for path_obj in model['paths'].values():
            for op in path_obj.values():
                op['responses'] = sorted_dict({**global_responses, **op['responses']}) if op[
                    'responses'] else global_responses
                self._fix_in_parameter_type(model, op)
        return model

    @staticmethod
    def _fix_in_parameter_type(
        api: dict,
        op: dict
    ) -> None:
        from jsonpointer import JsonPointer

        for parameter in op.get('parameters', ()):
            if schema := parameter['schema']:
                if '$ref' in schema:
                    schema = JsonPointer(schema['$ref']).to_last(api)

                name = parameter['name']
                if re.search(r'(?<!or)_isnull\b', name):
                    schema['type'] = 'boolean'
                elif name.endswith('_duration'):
                    parameter['schema']={'$ref':'#/components/schemas/TaskDuration'}
                else:
                    if re.search(r"(?<!external_)(?<!google_place_)(id|^id)($|_)", name):
                        if (schema := parameter.get('schema')) and schema.get('type') == 'string':
                            schema['format'] = 'uuid'

                    elif re.search(r'^([a-z_]+_at|[a-z_]+_after|[a-z_]+_before|end_time|start_time)(?!__date)($|__)', name):
                        schema['format'] = 'date-time'

                    elif re.search(r'_count($|_)', name):
                        schema['type'] = 'integer'

                    if re.search(r"__in(_or_is_null)?$", name):
                        if (schema := parameter.get('schema')) and schema.get('type') != 'array':
                            parameter['schema'] = {
                                'type': 'array',
                                'items': schema,
                            }
                            parameter['explode'] = False
