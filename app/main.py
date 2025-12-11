from litestar import Litestar
from litestar.openapi.config import OpenAPIConfig
from litestar.openapi.plugins import ScalarRenderPlugin

from app.config import sql_alchemy_plugin, structlog_plugin
from app.domain.dictionary.controllers import DatabaseController

app = Litestar(
    route_handlers=[DatabaseController],
    plugins=[sql_alchemy_plugin, structlog_plugin],
    # debug=True,
    openapi_config=OpenAPIConfig(
        title="IFT (API)",
        description="API for database management with integrated search functionality",
        version="0.0.1",
        render_plugins=[ScalarRenderPlugin()],
    ),
)
