
old_verison =['59', 'R8.2-LA', 'R11_LA', 'ServerPR7721', 'ServerPR7783-348ade', 'StatsPR842-0ce2e7', 'R1', '517', '1249', 'R8-latest', 'ServerPR7784-7acb87', 'ServerPR7805', 'R1_AVRS', 'R8.3-TEF-INF-17282', 'ServerPR7645-52b65d', 'ServerPR7730-12e24e', 'ServerPR7784', '1087', '104', 'current', 'APIPR1453-441cb6', 'R12_FEATURE_DEMO', '1489', '1310', 'R2', '643', 'APIPR1453', 'ServerPR7730', 'ServerPR7793-a2066b', '1510', '176', 'alarmInfraPhase1-1', 'ServerPR7645', '1269', 'ServerPR7793', 'ServerPR7799-531129', 'R3_NSG', 'alarmInfraPhase1', '1251', '721', '1491', 'ServerPR7799', 'R3', 'R6.9_LA-364.2', 'ServerPR7668-21fea9', 'ServerPR7735-aa09e3', '1492', '1511', '239', 'R6.9-EA-BT', 'ServerPR7668', 'R9-latest', '1294', 'ServerPR7765-5d0200', 'R4', 'R6.9_LA-364.3', 'ServerPR7691-7fa6f0', 'ServerPR7735', '1494', 'StatsPR842', 'R5_Beta', 'R9-latest_b', 'ServerPR7691', 'ServerPR7689-fcf3df', 'APIPR1462-856da7', '1513', '301', 'R9-latest_s', 'ServerPR7681-29afec', 'ServerPR7689', 'ServerPR7751-b54254', 'ServerPR7785-5eb0f9', 'R5', 'R9-latest_n', 'ServerPR7681', 'R12-current', '1495', 'ServerPR7806-69945b', 'R5.1', 'R6.9_LA', 'NSG_FALCON_DEMO', '1451', 'ScalePR1722-746963', 'ServerPR7806', '353', '677', 'ServerPR7711-34cbda', 'R12', '1497', '1514', 'R6_BETA_FOR_BT_INF16194', '523', 'ScalePR1739-909edd', 'ServerPR7734-e5897d', '1490', 'ScalePR1753-3f6745', 'R6', 'R9.1', 'ScalePR1739', 'ServerPR7734', 'APIPR1468-bc0934', 'ServerPR7765', 'R6.1_U1-364.1', 'R9.2_LA', 'ServerPR7711', '1456', 'APIPR1462', '1314', 'R6.1_U1', 'R8.3', 'ServerPR7700-bf973d', 'ServerPR7757-b61f08', 'ServerPR7802-4d14b7', 'ScalePR1753', 'R6.3_VNS_Only_GA', '698', 'StatsPR817-4332e0', 'R10', 'ServerPR7802', 'R12-latest', '429', 'R9.3_LA', 'StatsPR817', 'ServerPR7757', 'ServerPR7737-5566ae', 'R11-latest', 'R7_NSG', 'R6.10_LA-364.4', 'ServerPR7716-c7b735', 'R9', 'ServerPR7751', '1090', 'R7_NSG_AWS', 'R6.10_LA', 'ServerPR7716', 'ServerPR7747-577261', 'R12.1_210WBX', '1515', 'R7', 'R9.4_LA', 'ServerPR7714-3dcbb2', 'ServerPR7747', 'R12.1', 'latest', 'R6.3-BT', 'R6.10_LA_INF-17715', 'ServerPR7714', '1476', 'ServerPR7737', 'ServerPR7785-de71ca', '493', '780', 'ServerPR7700', 'ServerPR7773-659e83', 'APIPR1468', 'ServerPR7785', 'R8_EARLY_BUILD', '781', '1267', 'ServerPR7773', 'ScalePR1722', '507', 'R10-latest', '531', '1289', '1508', 'R8', 'R10-Beta-PXS', 'ServerPR7728-5f9eae', '1482', 'ServerPR7806-d639fe', 'R8.1', '1032', 'ServerPR7728', '1483', 'ServerPR7805-25fadd', '516', 'R11_LA_from', 'ServerPR7721-e51661', 'ServerPR7783', '1509']

import re
for i in old_verison:
    version_check = i.split("-")[0]
    if not (version_check.startswith("latest") or "PR" in version_check):
        patt = "^R(\d+)"
        try:
            if 3 < int(re.search(patt, version_check).group(1)) < 13:
                print("This image belongs to R4 - R12", i)
            else:
                print("This image not belongs to R4 - R12", i)
        except:
            print("give is oher vberison", i)
    else:
        print("This all PR and latest image ", i)
