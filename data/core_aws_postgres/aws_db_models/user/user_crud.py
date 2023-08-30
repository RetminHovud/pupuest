


from sqlmodel import Session

from data.core_aws_postgres.aws_db_models.user.user import User


def get_user_by_id(session: Session, id_user: int):
    return session.get(User, id_user)