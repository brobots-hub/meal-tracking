from dotenv import load_dotenv
from os import environ, path


def load_config(env_dir=''):
    env = environ.get('ENVIRONMENT')

    if env == 'DEVELOPMENT':
        return load_dotenv(
            dotenv_path=path.join(env_dir, '.env.dev'),
            override=True
        )

    else:
        return load_dotenv(
            dotenv_path=path.join(env_dir, '.env'),
            override=True
        )
