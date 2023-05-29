from propan import RedisBroker
from propan.fastapi.core.router import PropanRouter


class RedisRouter(PropanRouter):
    broker_class = RedisBroker
    broker: RedisBroker