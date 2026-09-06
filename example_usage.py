from client import AsyncUnhandledPromiseRejectionTriagerClient

def main():
    client = AsyncUnhandledPromiseRejectionTriagerClient()
    res = client.triage_async_concurrency_hazards()
    print('Async Concurrency Triager: ' + res['triage_id'] + ' (' + res['file_path'] + ')')
    print('Floating Promises: ' + str(res['floating_unawaited_promises_found']) + ' | Grade: ' + res['concurrency_safety_grade'])
    print('Dossier URL: ' + res['audit_dossier_url'])

if __name__ == '__main__':
    main()
