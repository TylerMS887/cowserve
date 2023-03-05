This is the Cowserve web server. It provides a secure cross-platform web server to serve friendly websites. The project itself is
called *Project Cowserve* and the application is a replacement for Apache2 (and [other servers][serverlist]).

[serverlist]: https://github.com/TylerMS887/cowserve/wiki/Comparison

## Install

For GNU/Linux or other UN\*X systems, just download `install-unix.sh`. For Windows, download `cowserve.exe` and add the directory to your
`PATH`.

You can also [get Cowserve onto other systems](https://github.com/TylerMS887/cowserve/wiki/Install).

## Usage

`cowserve [--port XX[XX]]`

`--port` should not contain any letters. Cowserve will render an error if it's not a valid `int` value.

Press <kbd>Ctrl</kbd> + <kbd>C</kbd> (<kbd>⌘</kbd> + <kbd>C</kbd> on a Mac) to end the server. This is useful in case of DoS or DDoS
attacks.

## Discussion

We mainly discuss the work for Cowserve at [GitHub Discussions](https://github.com/TylerMS887/cowserve/discussions).

Note that questions about **using** Cowserve are off-topic and should be asked at [Server Fault](https://serverfault.com). When the server has crashed, use the [<kbd>server-crashes</kbd>](https://serverfault.com/questions/tagged/server-crashes) tag. For questions most likely caused by a (D)DoS attack, use the [<kbd>ddos</kbd>](https://serverfault.com/questions/tagged/ddos) or [<kbd>denial-of-service</kbd>](https://serverfault.com/questions/tagged/denial-of-service) tag.

## Links
* [ServerFault](https://serverfault.com/questions/tagged/cowserve-http-server)
* [Cowserve Wiki](https://github.com/TylerMS887/cowserve/wiki)
