# Shepherd
**Built for python2.7**

Shepherd is a search & replace tool that takes parameters from a json file and injects them into your files. It was built primarily for use with Docker. It enables you to build a Docker container with a default template for your configuration files and then easily inject the configuration into those templates at runtime. This enables you to run Docker containers in different environments without the need to rebuild the container for each environment.

### Usage
To use Shepherd, the config is set inside of a JSON file. We create objects with the names of the files we want to edit and then set each property's key as the find string and the value as the replace string.

```json
{
    "/opt/application/config/config.ini": {
        "SHEP_DB_HOST": "db.example.com",
        "SHEP_DB_PASS": "P855W0RD"
    },
    "/etc/php5/fpm/php.ini": {
        "session.name = PHPSESSID": "session.name = MYSESSID"
    }
}
```

To run shepherd using the config file above, use the following command
```bash
shepherd -c /path/to/file.json
```
Shepherd also accepts a JSON string instead of a file path
```bash
shepherd -c '{"/tmp/myfile":{"REPLACETHIS":"WITHTHIS"}}'
```

### Commands

    [-h,--help]          shows this help information
    [-v,--version]       Shows the version of Python and Shepherd
    [-c,--config]        pass the applications config as a file path or a JSON string

