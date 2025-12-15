from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr, computed_field


class AppSettings(BaseSettings):
    APP_NAME: str = "FastAPI app"
    APP_DESCRIPTION: str | None = None
    APP_VERSION: str | None = None
    LICENSE_NAME: str | None = None
    CONTACT_NAME: str | None = None
    CONTACT_EMAIL: str | None = None


class CryptSettings(BaseSettings):
    SECRET_KEY: SecretStr # = SecretStr("YOUR-SECRET-KEY")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7


class SQLiteSettings(BaseSettings):
    SQLITE_FILENAME: str = "boilerplate.db"
    SQLITE_SYNC_PREFIX: str = "sqlite:///"
    SQLITE_ASYNC_PREFIX: str = "sqlite+aiosqlite:///"
    CONNECT_ARGS = {"check_same_thread": False}

    @computed_field
    @property
    def SQLITE_URL(self) -> str:
        return f"{self.SQLITE_SYNC_PREFIX}@{self.SQLITE_FILENAME}"


class PostgresSettings(BaseSettings):
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = "postgres"
    POSTGRES_SYNC_PREFIX: str = "postgresql://"
    POSTGRES_ASYNC_PREFIX: str = "postgresql+asyncpg://"
    POSTGRES_URL: str | None = None

    @computed_field
    @property
    def POSTGRES_URI(self) -> str:
        credentials = f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
        location = f"{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        return f"{credentials}@{location}"


class CORSSettings(BaseSettings):
    CORS_ORIGINS: list[str] = ["*"]
    CORS_METHODS: list[str] = ["*"]
    CORS_HEADERS: list[str] = ["*"]


class Settings(
    AppSettings,
    CryptSettings,
    SQLiteSettings,
    PostgresSettings,
    CORSSettings,
):
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True) 
    # env_file=os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..", ".env"),


settings = Settings()
