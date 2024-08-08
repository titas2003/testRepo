import logsrvasst as asst
# Load properties from JSON file
# port = input("Enter port number:")
# protocol = input("Enter protocol")
# print(asst.logsrvasst(port,protocol))
# if(port != 514):
#     asst.print_suggestions(port,protocol)
 json_file_path = 'properties.json'
 properties = asst.load_properties(json_file_path)
    
# # Show property descriptions
 property_descriptions_json = asst.show_property_descriptions(properties)
 print("\nProperty descriptions in JSON format:")
# # print(property_descriptions_json)
    
# # User input
 template_name = input("Enter the template name: ")
 file_path = input("Enter the file path: ")

# # Generate the rsyslog template
 rsyslog_template = asst.generate_template(template_name, file_path, properties)
    
# # Print the generated template
# print("\nGenerated rsyslog template:")
# print(rsyslog_template)
# ruleset generator
rsyslog_ruleset = asst.create_rsyslog_ruleset('testRule', 'exampleTemplate', 514, 'udp', '*.info,mail.crit')
print(rsyslog_ruleset)
# tls ruleset generator
# tls_ruleset = asst.create_tls_rsyslog_ruleset("Test_Rule","Test_template",514,"/etc/CA.pem","/etc/tls.pem","/etc/tls.key","local3.info,local4.*")
# print(tls_ruleset)
