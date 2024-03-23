CREATE TABLE IF NOT EXISTS "user"
(
    "id"              INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "email"           VARCHAR(255) NOT NULL UNIQUE,
    "first_name"      VARCHAR(255) NOT NULL,
    "last_name"       VARCHAR(255) NOT NULL,
    "hashed_password" BLOB         NOT NULL /* User hashed password */,
    "last_login"      TIMESTAMP    NOT NULL
) /* Main user model */;
CREATE INDEX IF NOT EXISTS "idx_user_email_1b4f1c" ON "user" ("email");
CREATE TABLE IF NOT EXISTS "session"
(
    "session_key"     VARCHAR(1024) NOT NULL PRIMARY KEY,
    "expire_at"       TIMESTAMP     NOT NULL /* Session expire timestamp */,
    "additional_data" JSON          NOT NULL,
    "user_id"         BIGINT        NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
) /* Session model to handle UI authorization */;
CREATE TABLE IF NOT EXISTS "client"
(
    "client_id"     VARCHAR(32)  NOT NULL PRIMARY KEY,
    "client_secret" BLOB         NOT NULL,
    "name"          VARCHAR(255) NOT NULL,
    "homepage"      VARCHAR(255) NOT NULL,
    "callback_url"  VARCHAR(255) NOT NULL,
    "created_at"    TIMESTAMP    NOT NULL,
    "owner_id"      BIGINT       NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
) /* Settings for authorization through our app */;
CREATE TABLE IF NOT EXISTS "migrate"
(
    "id"   INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "file" VARCHAR(1024) NOT NULL
);