# Generated by Lapidary.
# All manual changes will be lost!

from __future__ import annotations

import typing
import lapidary.runtime
import pydantic
import enum


class RecipientEnum(enum.Enum):
    account = "account"
    assignee = "assignee"
    orderer = "orderer"
    contact = "contact"
    client = "client"