config: dict[str, str | bool | int] = {
    "host": "192.168.1.1",
    "port": 8080,
    "ssl": True,
    "timeout": 30
}
print(f"Host: {config["host"]}")
config["port"] = 443
config["protocol"] = "https"
print(config)