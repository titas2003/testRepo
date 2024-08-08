import logcliasst as assist
print(assist.client_ruleset_config("test_rule","localhost",524,"tcp"))
print(assist.apply_ruleset_client("/var/log/message.log","test","local3","info","test_rule"))
print(assist.client_tls_template("/etc/cert.pem","localhost","tcp",524,"test_rule"))
