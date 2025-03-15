function FindProxyForURL(url, host) {
    if (shExpMatch(host, "*m")) {
        return "PROXY https://solid-doodle-v64x6x9j757hxqr7.github.dev/:8080";
    } else {
        return "DIRECT";
    }
}
