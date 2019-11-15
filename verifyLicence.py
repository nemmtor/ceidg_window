from turboactivate import (
    TurboActivate,
    IsGenuineResult,
    TurboActivateError,
    TurboActivateTrialExpiredError,
    TA_USER,
    TA_SYSTEM
)


DAYS_BETWEEN_CHECKS = 0
GRACE_PERIOD_LENGTH = 0
isGenuine = False
try:
    ta = TurboActivate("s3zjitggmosjwplknuelsytyhfavnzi", TA_SYSTEM)
    gen_r = ta.is_genuine_ex(DAYS_BETWEEN_CHECKS, GRACE_PERIOD_LENGTH, True)
    isGenuine = (gen_r == IsGenuineResult.Genuine
                         or gen_r == IsGenuineResult.GenuineFeaturesChanged

                         # an internet error means the user is activated but
                         # TurboActivate failed to contact the LimeLM servers
                         or gen_r == IsGenuineResult.InternetError
                         )
    if not isGenuine and ta.is_activated():
        print('You must reverify with the activation servers before you can use this app. ')
        print('Type R and then press enter to retry after you\'ve ensured that you\'re connected to the internet. ')
        print('Or to exit the app press X. ')

        while True:
            user_resp = sys.stdin.read(1)

            if user_resp == 'x' or user_resp == 'X':
                sys.exit("Exiting now. Bye.")

            if user_resp == 'r' or user_resp == 'R':
                # Now we're using TA_IsGenuine() to retry immediately. Note that we're not using
                # TA_IsGenuineEx() because TA_IsGenuineEx() waits 5 hours after an internet failure
                # before retrying to contact the servers. TA_IsGenuine() retries immediately.
                igr = ta.is_genuine()

                if igr == IsGenuineResult.Genuine or igr == IsGenuineResult.GenuineFeaturesChanged:
                    print('Successfully reverified with the servers! You can now continue to use the app!')
                    break
                else:
                    print('Failed to reverify with the servers. ')
                    print('Make sure you\'re connected to the internet and that you\'re not blocking access to the activation servers. ')
                    print('Then press R to retry again. ')
            else:
                print('Invalid input. Press R to try to reverify with the servers. Press X to exit the app.')
except TurboActivateError as e:
    sys.exit("Failed to check if activated: " + str(e))
