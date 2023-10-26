# GrimoireLabDeployments
A repository of Grimoirelab deployment configs for various projects

## Troubleshooting

If you run into the below error with elasticsearch:

```
java.lang.UnsupportedOperationException: seccomp unavailable: CONFIG_SECCOMP not compiled into kernel, CONFIG_SECCOMP and CONFIG_SECCOMP_FILTER are needed
```

You can turn off [system call filters](https://www.elastic.co/guide/en/elasticsearch/reference/7.17/_system_call_filter_check.html)
**at your own risk**:

> Elasticsearch installs system call filters of various flavors depending on the operating system (e.g., seccomp on Linux). These system call filters are installed to prevent the ability to execute system calls related to forking as a defense mechanism against arbitrary code execution attacks on Elasticsearch. The system call filter check ensures that if system call filters are enabled, then they were successfully installed. To pass the system call filter check you must either fix any configuration errors on your system that prevented system call filters from installing (check your logs), or at your own risk disable system call filters by setting bootstrap.system_call_filter to false.

In order to turn it off, change the following line in docker-compose.yml:

```
command: elasticsearch -Enetwork.bind_host=0.0.0.0 -Ehttp.max_content_length=2000mb
```

to

```
command: elasticsearch -Enetwork.bind_host=0.0.0.0 -Ehttp.max_content_length=2000mb -Ebootstrap.system_call_filter=false
```
