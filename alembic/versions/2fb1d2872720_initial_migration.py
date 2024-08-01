"""Initial migration

Revision ID: 2fb1d2872720
Revises: 
Create Date: 2024-08-01 11:47:56.326120

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from passlib.context import CryptContext


# revision identifiers, used by Alembic.
revision: str = '2fb1d2872720'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# Configuração do Passlib para hash da senha
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Função para gerar hash da senha
def get_password_hash(password):
    return pwd_context.hash(password)

def upgrade():
    # Código para adicionar o usuário inicial
    conn = op.get_bind()
    hashed_password = get_password_hash("123456*a1")
    conn.execute(
        sa.text(
            "INSERT INTO users (username, email, hashed_password) VALUES (:username, :email, :hashed_password)"
        ),
        username="trcarneiro",
        email="email_inicial@example.com",
        hashed_password=hashed_password
    )

def downgrade():
    # Código para remover o usuário inicial
    conn = op.get_bind()
    conn.execute(
        sa.text(
            "DELETE FROM users WHERE username = :username"
        ),
        username="usuario_inicial"
    )