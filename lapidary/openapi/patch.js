/**
 * Update multiple properties of the target object with a value
 */
function updateProperties(properties, value) {
    function _(target) {
        for (const prop of properties) target[prop] = {...target[prop], ...value};
        return target;
    }

    return _;
}

// add some missing types
replace('$.components.schemas', schemas => ({
    ...schemas,
    GSMTasksError: {
        type: 'object',
        properties: {
            detail: {
                type: 'string',
            },
        },
        required: ['detail'],
        additionalProperties: false,
    },
    Metafields: {
        type: 'object',
    },
    NullableTaskDuration: {
        title: 'Nullable task duration',
        anyOf: [
            {type: 'string'},
            {
                type: 'integer',
                nullable: true,
            },
        ],
    },
    TaskDuration: {
        title: 'Task duration',
        anyOf: [{type: 'string'}, {type: 'integer'}],
    },
    TaskListExt: {
        type: 'object',
        properties: {
            tasks: {$ref: '#/components/schemas/PaginatedTaskSerializerV2List'},
            documents: {$ref: '#/components/schemas/PaginatedDocumentList'},
            metadatas: {$ref: '#/components/schemas/PaginatedTaskMetadataList'},
        },
        required: ['tasks'],
    },
    ValidationError: {
        type: 'object',
        additionalProperties: {
            type: 'array',
            items: {
                type: 'string',
            },
        },
    },
}));

// update some schemas

replace('$.components.schemas.Account.properties', props => ({
    ...props,
    stripe_payment_method_id: {
        ...props.stripe_payment_method_id,
        nullable: true,
    },
    stripe_customer_id: {
        ...props.stripe_customer_id,
        nullable: true,
    },
    task_duration: {$ref: '#/components/schemas/TaskDuration'},
    feature_geocoding_country_code: {
        anyOf: [{$ref: '#/components/schemas/CountryCodeEnum'}, {$ref: '#/components/schemas/BlankEnum'}],
        readOnly: true,
        description: 'Limit geocoding to the selected country.',
    },
}));

replace(
    '$.components.schemas.AccountRole.properties',
    updateProperties(['signature_image', 'last_time_location', 'deleted_at', 'activated_at'], {nullable: true}),
);

replace(
    '$.components.schemas.Document.properties',
    updateProperties(['file_name', 'mimetype', 'thumbnail'], {nullable: true}),
);

replace('$.components.schemas.TaskCommand', schema => ({
    ...schema,
    additionalProperties: false,
}));

replace('$.components.schemas.Metafield', schema => ({
    ...schema,
    description: `At least one of:
- show_in_list_view
- show_in_detail_view
- show_in_mobile_app
- show_in_pod
is required`,
}));

// fix nullability for properties with null values in live responses
replace(
    '$.components.schemas.NestedAddress.properties',
    updateProperties(['geocoded_at', 'failed_at'], {nullable: true}),
);

replace('$.components.schemas.TaskSerializerV2', schema => {
    updateProperties(['cancelled_at', 'completed_at', 'orderer_name', 'recurrence'], {nullable: true})(schema.properties);
    schema.properties.duration = {$ref: '#/components/schemas/TaskDuration'};
    schema.properties.actions = {
        type: 'array',
        readOnly: true,
        items: {
            type: 'string',
        },
    };
    schema.additionalProperties = false;
    return schema;
});

replace(
    '$.components.schemas.TaskMetadata.properties',
    updateProperties(
        [
            'assigned_duration',
            'unassigned_duration',
            'accepted_duration',
            'transit_duration',
            'active_duration',
            'completed_duration',
            'failed_duration',
            'cancelled_duration',
        ],
        {$ref: '#/components/schemas/NullableTaskDuration'},
    ),
);

// fix types

replace('$.components.schemas.TrackerPublic.properties.queue_positions.items.type', _ => 'integer');

replace('$..metafields', _ => ({$ref: '#/components/schemas/Metafields'}));

// fix schemas in paths

replace('$.paths["/documents/"].post.requestBody.content["application/json"].schema', _ => ({
    anyOf: [{$ref: '#/components/schemas/PaginatedDocumentList'}, {$ref: '#/components/schemas/Document'}],
    additionalProperties: false,
}));

replace(
    '$.paths["/documents/"].post.responses["201"].content[?match(#, "application/json; version=.*")].schema',
    _ => ({
        anyOf: [{$ref: '#/components/schemas/PaginatedDocumentList'}, {$ref: '#/components/schemas/Document'}],
        additionalProperties: false,
    }),
);

replace(
    '$.paths["/file_uploads/"].post.responses["201"].content[?match(#, "application/json; version=.*")].schema',
    _ => ({
        anyOf: [
            {
                $ref: '#/components/schemas/PaginatedS3FileUploadList',
            },
            {
                $ref: '#/components/schemas/S3FileUpload',
            },
        ],
        additionalProperties: false,
    }),
);

replace('$.paths["/file_uploads/"].post.requestBody.content["application/json"].schema', _ => ({
    anyOf: [
        {
            $ref: '#/components/schemas/PaginatedS3FileUploadList',
        },
        {
            $ref: '#/components/schemas/S3FileUpload',
        },
    ],
    additionalProperties: false,
}));

replace(
    [
        '$.paths["/task_commands/"].post.requestBody.content["application/json"].schema',
        '$.paths["/task_commands/"].post.responses["201"].content[?match(#, "application/json; version=.*")].schema',
    ],
    _ => ({
        anyOf: [
            {
                $ref: '#/components/schemas/TaskCommand',
            },
            {
                type: 'array',
                items: {$ref: '#/components/schemas/TaskCommand'},
            },
        ],
    }),
);

replace(
    [
        '$.paths["/tasks/"].get.responses["200"].content[?match(#, "application/json; version=.*")].schema',
        '$.paths["/tasks/"].post.responses["201"].content[?match(#, "application/json; version=.*")].schema',
        '$.paths["/tasks/"].post.requestBody.content["application/json"].schema',
    ],
    _ => ({
        anyOf: [
            {$ref: '#/components/schemas/PaginatedTaskSerializerV2List'},
            {$ref: '#/components/schemas/TaskListExt'},
        ],
    }),
);

// add error responses
replace('$.components', components => ({
    ...components,
    responses: {
        'generic-error': {
            content: {
                'application/json': {
                    schema: {$ref: '#/components/schemas/GSMTasksError'},
                },
            },
            description: 'Generic error',
        },
        'validation-error': {
            content: {
                'application/json': {
                    schema: {
                        $ref: '#/components/schemas/ValidationError',
                    },
                },
            },
            description: 'Validation error',
        },
    },
}));

// fix schemas

replace(['$..[?@.setup_intent]'], props => ({properties: props}));

replace(['$..[?@.schema.token]', '$..[?@.schema.default_payment_method_id]'], value => ({
    ...value,
    schema: {
        type: 'object',
        properties: value.schema,
    },
}));

// remove uuid examples and replace date-time examples with constant value
replace('$..[?@.example]', schema => {
    if (!('example' in schema) || typeof schema.example !== 'string') return schema;
    let example = schema.example;
    if (/[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}/.test(example)) {
        delete schema.example;
        return schema;
    } else if (/[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}[+-][0-9]{2}:[0-9]{2}/.test(schema.example))
        example = example.replace(
            /[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}[+-][0-9]{2}:[0-9]{2}/g,
            '2000-01-01T00:00:00+00:00',
        );

    schema.example = example;
    return schema;
});

// apply the error responses to all operations
replace('$.paths..responses', responses => ({
    ...responses,
    '400': {$ref: '#/components/responses/validation-error'},
    '4XX': {$ref: '#/components/responses/generic-error'},
    '5XX': {$ref: '#/components/responses/generic-error'},
}));

// add next link header to all "*_list" operations
replace('$.paths[*][?search(@.operationId,"_list")].responses["200"]', response => {
    return {
        ...response,
        headers: {
            link: {
                schema: {
                    type: 'array',
                    items: {type: 'string'},
                },
                explode: false,
            },
        },
    };
});

// fix schema in __isnull parameters
replace('$..parameters[?search(@.name, "__isnull$")].schema', _ => ({type: 'boolean'}));

// fix schema in _duration parameters
replace('$..parameters[?search(@.name, "_duration$")].schema', _ => ({$ref: '#/components/schemas/TaskDuration'}));

// add format to some _id parameters
replace(
    [
        ...[
            'assignee_id',
            'contact_id',
            'order_id',
            'orderer_id',
            'owner_id',
            'receiver_id',
            'route_id',
            'unassignee_id',
            'address_id',
        ].flatMap(name => [`$..parameters[?@.name == "${name}"]`, `$..parameters[?@.name == "${name}__in"]`,]),
        '$..parameters[?@.name == "id__in"]',
    ],
    param => ({
        ...param,
        schema: {
            type: 'string',
            format: 'uuid',
        },
    }),
);

// fix date-time format
replace('$..schema.format', format => format.replace('datetime', 'date-time'));

// fix schema in _count parameters
replace('$..[?search(@.name,"_count($|_)")]', param => ({
    ...param,
    schema: {type: 'integer'},
    description: '',
}));

// fix schema for `__in`-like parameters
replace('$..[?search(@.name,"__in|__not_in|__in_or_null|__not_in_or_null")]', param => ({
    ...param,
    schema: {
        type: 'array',
        items: param.schema,
    },
    explode: false,
}));

// TODO offer better schemas
replace(['$..attached_payment_methods', '$..default_payment_method_id'], _ => ({}))
