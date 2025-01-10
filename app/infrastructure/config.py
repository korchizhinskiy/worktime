import logging
from pathlib import Path, PosixPath

from pydantic.functional_validators import field_validator
from pydantic.main import BaseModel
from pydantic_settings.main import BaseSettings, SettingsConfigDict

type PublicKeyPath = str
type PrivateKeyPath = str
type Certificate = str
type AlgorithmName = str

BASE_DIR = Path(__file__).parent.parent.parent


class DatabaseConnectionSettings(BaseModel):
    database_user: str
    database_name: str
    database_password: str
    database_host: str
    database_port: int


class CryptoSettings(BaseModel):
    public_key: PublicKeyPath
    private_key: PrivateKeyPath
    algorithm: AlgorithmName = "RS256"

    @field_validator("public_key", "private_key", mode="before")
    @classmethod
    def load_file_content(cls, value: PosixPath) -> Certificate:
        try:
            return Path(BASE_DIR / value).read_text(encoding="utf-8").strip()
        except IsADirectoryError as error:
            raise ValueError("You must define path to file, not to directory.") from error
        except FileNotFoundError as error:
            raise ValueError("This path ot file is not found.") from error


class CommonSettings(BaseModel):
    log_level: int

    @field_validator("log_level", mode="before")
    @classmethod
    def validate_log_level(cls, value: str) -> int:
        try:
            return logging.getLevelNamesMapping()[value]
        except KeyError as error:
            raise ValueError(f"Logging level with name {value} is not found in {logging!r} module") from error


class Settings(BaseSettings):
    certs: CryptoSettings
    db_connection: DatabaseConnectionSettings
    common: CommonSettings
    model_config = SettingsConfigDict(env_file=(".env",), env_nested_delimiter="__", str_to_lower=True)
