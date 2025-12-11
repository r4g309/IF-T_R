from litestar.config.cors import CORSConfig
from litestar.plugins.sqlalchemy import (
    AsyncSessionConfig,
    EngineConfig,
    SQLAlchemyAsyncConfig,
    SQLAlchemyInitPlugin,
)
from litestar.plugins.structlog import StructlogConfig, StructlogPlugin

async_session_config = AsyncSessionConfig(expire_on_commit=False)


database_config = SQLAlchemyAsyncConfig(
    connection_string="sqlite+aiosqlite:///database.sqlite",
    engine_config=EngineConfig(echo=True),
    session_config=async_session_config,
    before_send_handler="autocommit_include_redirects",
    create_all=True,
)


cors_config = CORSConfig(
    allow_origins=["*"],
    allow_methods=["GET", "POST", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["*"],
    expose_headers=["Authorization"],
)


structlog_config = StructlogConfig()


structlog_plugin = StructlogPlugin(config=structlog_config)


sql_alchemy_plugin = SQLAlchemyInitPlugin(config=database_config)
