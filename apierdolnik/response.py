from typing import Any

from pydantic import BaseModel, validator


class Response(BaseModel):
    body: Any
    status_code: int

    @validator('status_code')
    def status_code_valid(cls, value):  # noqa
        assert value in [
            100, 101, 102, 103, 200, 201, 202, 203, 204, 205, 206, 207, 226, 300, 301, 302, 303, 304, 305, 306, 307,
            308, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 415, 416, 417, 418, 421, 422,
            423, 424, 425, 426, 428, 429, 431, 451, 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511
        ], 'invalid status code'
        return value
