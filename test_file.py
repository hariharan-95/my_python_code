
explain_json = requests.get("http://badcvtb59.ba.nuagenetworks.net: 9200/nuage_flow*/_ilm/explain", verify=False)

assert explain_json.status_code == 200, "Could not fetch ILM explain details"
explain_dict = explain_json.json()
print(explain_dict)

