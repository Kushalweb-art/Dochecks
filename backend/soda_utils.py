import os
from soda.scan import Scan
from dotenv import load_dotenv

load_dotenv()

def run_soda_scan(database_url, table_name):
    scan = Scan()
    scan.set_data_source_name("my_database")
    scan.add_configuration_yaml_file("backend/soda_checks.yml")
    scan.set_data_source_connection_url(database_url)
    scan.add_sodacl_yaml_file("backend/soda_checks.yml")

    scan.execute()

    results = []
    for check in scan.get_checks():
        results.append({
            "table": table_name,
            "column": check.metrics.get("column") if check.metrics else None,
            "check_name": check.name,
            "status": "Pass" if check.outcome == "PASS" else "Fail",
        })
    
    return results
