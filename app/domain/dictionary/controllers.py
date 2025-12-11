from typing import TYPE_CHECKING

from advanced_alchemy.service.pagination import OffsetPagination
from litestar import Controller, get, post
from litestar.di import Provide

from app.domain.dictionary.dependencies import provide_databases_service
from app.domain.dictionary.schemas import Database, DatabaseCreate
from app.domain.dictionary.services import DatabaseService

if TYPE_CHECKING:
    from advanced_alchemy.service.pagination import OffsetPagination


class DatabaseController(Controller):
    tags = ("Databases",)
    path = "/databases/"
    dependencies = {"databases_service": Provide(provide_databases_service)}

    @get(
        path="/",
        name="databases.list",
        operation_id="ListDatabases",
        component="database/list",
    )
    async def list_databases(
        self,
        databases_service: DatabaseService,
    ) -> OffsetPagination[Database]:
        """List all databases."""
        results, total = await databases_service.list_and_count()
        return databases_service.to_schema(
            data=results, total=total, schema_type=Database
        )

    @post(
        path="/",
        name="databases.add",
        operation_id="CreateDatabase",
    )
    async def create_database(
        self,
        data: DatabaseCreate,
        databases_service: DatabaseService,
    ) -> Database:
        """Create a new database."""
        obj = data.model_dump()
        db_obj = await databases_service.create(obj)
        return databases_service.to_schema(schema_type=Database, data=db_obj)

    # @post(
    #     name="teams.add",
    #     operation_id="CreateTeam",
    #     summary="Create a new team.",
    #     path="/teams/",
    # )
    # async def create_team(
    #     self,
    #     request: Request,
    #     teams_service: TeamService,
    #     current_user: UserModel,
    #     data: TeamCreate,
    # ) -> InertiaRedirect:
    #     """Create a new team."""
    #     obj = data.to_dict()
    #     obj.update({"owner_id": current_user.id, "owner": current_user})
    #     db_obj = await teams_service.create(obj)
    #     flash(request, f'Successfully created team "{db_obj.name}".', category="info")
    #     return InertiaRedirect(
    #         request, request.url_for("teams.show", team_id=db_obj.id)
    #     )

    # @get(
    #     component="team/show",
    #     name="teams.show",
    #     operation_id="GetTeam",
    #     guards=[requires_team_membership],
    #     path="/teams/{team_id:uuid}/",
    # )
    # async def get_team(
    #     self,
    #     request: Request,
    #     teams_service: TeamService,
    #     team_id: Annotated[
    #         UUID,
    #         Parameter(
    #             title="Team ID",
    #             description="The team to retrieve.",
    #         ),
    #     ],
    # ) -> Team:
    #     """Get details about a team."""
    #     db_obj = await teams_service.get(team_id)
    #     request.session.update(
    #         {"currentTeam": {"teamId": db_obj.id, "teamName": db_obj.name}}
    #     )
    #     return teams_service.to_schema(schema_type=Team, data=db_obj)

    # @patch(
    #     component="team/edit",
    #     name="teams.edit",
    #     operation_id="UpdateTeam",
    #     guards=[requires_team_admin],
    #     path="/teams/{team_id:uuid}/",
    # )
    # async def update_team(
    #     self,
    #     request: Request,
    #     data: TeamUpdate,
    #     teams_service: TeamService,
    #     team_id: Annotated[
    #         UUID,
    #         Parameter(
    #             title="Team ID",
    #             description="The team to update.",
    #         ),
    #     ],
    # ) -> Team:
    #     """Update a migration team."""
    #     db_obj = await teams_service.update(
    #         item_id=team_id,
    #         data=data.to_dict(),
    #     )
    #     request.session.update(
    #         {"currentTeam": {"teamId": db_obj.id, "teamName": db_obj.name}}
    #     )
    #     return teams_service.to_schema(schema_type=Team, data=db_obj)

    # @delete(
    #     name="teams.remove",
    #     operation_id="DeleteTeam",
    #     guards=[requires_team_ownership],
    #     path="/teams/{team_id:uuid}/",
    #     status_code=303,  # This is the correct inertia redirect code
    # )
    # async def delete_team(
    #     self,
    #     request: Request,
    #     teams_service: TeamService,
    #     team_id: Annotated[
    #         UUID,
    #         Parameter(title="Team ID", description="The team to delete."),
    #     ],
    # ) -> InertiaRedirect:
    #     """Delete a team."""
    #     request.session.pop("currentTeam")
    #     db_obj = await teams_service.delete(team_id)
    #     flash(request, f'Removed team "{db_obj.name}".', category="info")
    #     return InertiaRedirect(request, request.url_for("teams.list"))
