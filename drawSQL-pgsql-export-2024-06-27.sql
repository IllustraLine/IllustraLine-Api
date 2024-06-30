CREATE TABLE "user"(
    "id" BIGINT NOT NULL,
    "email" VARCHAR(255) NOT NULL,
    "username" VARCHAR(255) NOT NULL,
    "password" VARCHAR(255) NULL,
    "is_active" BOOLEAN NOT NULL DEFAULT '0',
    "is_admin" BOOLEAN NOT NULL DEFAULT '0',
    "created_at" FLOAT(53) NOT NULL,
    "updated_at" FLOAT(53) NOT NULL,
    "banned_at" FLOAT(53) NULL,
    "unbanned_at" FLOAT(53) NULL,
    "profile_name" VARCHAR(255) NOT NULL,
    "profile_image" bytea NOT NULL
);
ALTER TABLE
    "user" ADD PRIMARY KEY("id");
ALTER TABLE
    "user" ADD CONSTRAINT "user_email_unique" UNIQUE("email");
ALTER TABLE
    "user" ADD CONSTRAINT "user_username_unique" UNIQUE("username");
CREATE TABLE "course"(
    "id" BIGINT NOT NULL,
    "title" VARCHAR(255) NOT NULL,
    "description" VARCHAR(255) NOT NULL,
    "artist" VARCHAR(255) NOT NULL,
    "category" VARCHAR(255) NOT NULL,
    "tags" jsonb NOT NULL DEFAULT '[]',
    "price" FLOAT(53) NOT NULL,
    "created_at" FLOAT(53) NOT NULL,
    "updated_at" FLOAT(53) NOT NULL,
    "is_active" BOOLEAN NOT NULL,
    "column_11" BIGINT NOT NULL,
    "image_name" VARCHAR(255) NOT NULL,
    "course_image" bytea NOT NULL,
    "admin_id" BIGINT NOT NULL,
    "admin_username" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "course" ADD PRIMARY KEY("id");
ALTER TABLE
    "course" ADD CONSTRAINT "course_title_unique" UNIQUE("title");
ALTER TABLE
    "course" ADD CONSTRAINT "course_admin_id_unique" UNIQUE("admin_id");
ALTER TABLE
    "course" ADD CONSTRAINT "course_admin_username_unique" UNIQUE("admin_username");
CREATE TABLE "admin_course"(
    "id" BIGINT NOT NULL,
    "user_id" BIGINT NOT NULL,
    "username" VARCHAR(255) NOT NULL,
    "created_at" FLOAT(53) NOT NULL,
    "updated_at" FLOAT(53) NOT NULL
);
ALTER TABLE
    "admin_course" ADD PRIMARY KEY("id");
ALTER TABLE
    "admin_course" ADD CONSTRAINT "admin_course_user_id_unique" UNIQUE("user_id");
ALTER TABLE
    "admin_course" ADD CONSTRAINT "admin_course_username_unique" UNIQUE("username");
CREATE TABLE "acoount_active"(
    "id" BIGINT NOT NULL,
    "user_id" BIGINT NOT NULL,
    "token" VARCHAR(255) NOT NULL,
    "created_at" FLOAT(53) NOT NULL,
    "updated_at" FLOAT(53) NOT NULL
);
ALTER TABLE
    "acoount_active" ADD PRIMARY KEY("id");
ALTER TABLE
    "acoount_active" ADD CONSTRAINT "acoount_active_user_id_unique" UNIQUE("user_id");
ALTER TABLE
    "acoount_active" ADD CONSTRAINT "acoount_active_token_unique" UNIQUE("token");
CREATE TABLE "wallet"(
    "id" BIGINT NOT NULL,
    "user_id" BIGINT NOT NULL,
    "is_active" BOOLEAN NOT NULL DEFAULT '1',
    "amount" FLOAT(53) NOT NULL DEFAULT '0',
    "created_at" FLOAT(53) NOT NULL,
    "updated_at" FLOAT(53) NOT NULL,
    "banned_at" FLOAT(53) NULL,
    "unbanned_at" FLOAT(53) NULL
);
ALTER TABLE
    "wallet" ADD PRIMARY KEY("id");
CREATE TABLE "my_course"(
    "id" BIGINT NOT NULL,
    "course_id" BIGINT NOT NULL,
    "created_at" FLOAT(53) NOT NULL
);
ALTER TABLE
    "my_course" ADD PRIMARY KEY("id");
ALTER TABLE
    "my_course" ADD CONSTRAINT "my_course_course_id_unique" UNIQUE("course_id");
CREATE TABLE "reset_password"(
    "id" BIGINT NOT NULL,
    "user_id" BIGINT NOT NULL,
    "token" VARCHAR(255) NOT NULL,
    "created_at" FLOAT(53) NOT NULL,
    "updated_at" FLOAT(53) NOT NULL
);
ALTER TABLE
    "reset_password" ADD PRIMARY KEY("id");
ALTER TABLE
    "reset_password" ADD CONSTRAINT "reset_password_user_id_unique" UNIQUE("user_id");
ALTER TABLE
    "reset_password" ADD CONSTRAINT "reset_password_token_unique" UNIQUE("token");
ALTER TABLE
    "course" ADD CONSTRAINT "course_admin_username_foreign" FOREIGN KEY("admin_username") REFERENCES "admin_course"("username");
ALTER TABLE
    "acoount_active" ADD CONSTRAINT "acoount_active_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "user"("id");
ALTER TABLE
    "my_course" ADD CONSTRAINT "my_course_course_id_foreign" FOREIGN KEY("course_id") REFERENCES "course"("id");
ALTER TABLE
    "admin_course" ADD CONSTRAINT "admin_course_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "user"("id");
ALTER TABLE
    "course" ADD CONSTRAINT "course_admin_id_foreign" FOREIGN KEY("admin_id") REFERENCES "admin_course"("id");
ALTER TABLE
    "reset_password" ADD CONSTRAINT "reset_password_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "user"("id");
ALTER TABLE
    "wallet" ADD CONSTRAINT "wallet_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "user"("id");