import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.relative_locator import locate_with

driver = webdriver.Firefox()
def tc_pim_01():
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.XPATH,"//input[@name='username']").send_keys('Admin')
    driver.find_element(By.XPATH,"//p[contains(.,'Forgot your password?')]").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@name='username']").send_keys('Admin')
    driver.find_element(By.XPATH,"//button[contains(.,'Reset Password')]").click()
    time.sleep(3)
    success = driver.find_element(By.XPATH,"//h6[contains(.,'Reset Password link sent successfully')]")
    x = success.text
    print(x)

def tc_pim_02():
    user_management = "User Management"
    job = "Job"
    organization = "Organization"
    qualifications = "Qualifications"
    nationalities = "Nationalities"
    corporate_branding = "Corporate Branding"
    configuration = "Configuration"
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR,"input[name='username']").send_keys('Admin')
    driver.find_element(By.CSS_SELECTOR,"input[name='password']").send_keys('admin123')
    driver.find_element(By.XPATH,"//button[@class = 'oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']").click()
    time.sleep(5)
    driver.find_element(By.LINK_TEXT,"Admin").click()
    time.sleep(3)
    um_output = driver.find_element(By.XPATH,"//span[starts-with(.,'User Management')]")
    job_output = driver.find_element(By.XPATH, "//span[starts-with(.,'Job')]")
    org_output = driver.find_element(By.XPATH,"//span[starts-with(.,'Organization')]")
    qual_output = driver.find_element(By.XPATH,"//span[starts-with(.,'Qualifications')]")
    nat_output = driver.find_element(By.XPATH, "//a[starts-with(.,'Nationalities')]")
    corp_output = driver.find_element(By.XPATH, "//a[starts-with(.,'Corporate Branding')]")
    config_output = driver.find_element(By.XPATH, "//span[starts-with(.,'Configuration')]")
    um_output = um_output.text
    job_output = job_output.text
    org_output = org_output.text
    qual_output = qual_output.text
    nat_output = nat_output.text
    corp_output = corp_output.text
    config_output = config_output.text

    if user_management == um_output:
        print(user_management)
    if job == job_output:
        print(job)
    if organization == org_output:
        print(organization)
    if qualifications == qual_output:
        print(qualifications)
    if nationalities == nat_output:
        print(nationalities)
    if corporate_branding == corp_output:
        print(corporate_branding)
    if configuration == config_output:
        print(configuration)
    else:
        print("Headers are not valid")

def tc_pim_03():
    admin = 'Admin'
    pim =  'PIM'
    leave = 'Leave'
    time1 = 'Time'
    recruitment = 'Recruitment'
    info = 'My Info'
    performance = 'Performance'
    dashboard = 'Dashboard'
    directory = 'Directory'
    maintenance = 'Maintenance'
    buzz = 'Buzz'

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys('Admin')
    driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys('admin123')
    driver.find_element(By.XPATH,"//button[@class = 'oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']").click()
    time.sleep(5)
    driver.find_element(By.LINK_TEXT, "Admin").click()
    time.sleep(3)
    admin_op = driver.find_element(By.XPATH,"//span[.='Admin']")
    pim_op = driver.find_element(By.XPATH, "//span[.='PIM']")
    leave_op = driver.find_element(By.XPATH, "//span[.='Leave']")
    time_op = driver.find_element(By.XPATH, "//span[.='Time']")
    rec_op = driver.find_element(By.XPATH, "//span[.='Recruitment']")
    info_op = driver.find_element(By.XPATH, "//span[.='My Info']")
    perf_op = driver.find_element(By.XPATH, "//span[.='Performance']")
    dash_op = driver.find_element(By.XPATH, "//span[.='Dashboard']")
    direc_op = driver.find_element(By.XPATH, "//span[.='Directory']")
    main_op = driver.find_element(By.XPATH, "//span[.='Maintenance']")
    buzz_op = driver.find_element(By.XPATH, "//span[.='Buzz']")

    admin_op = admin_op.text
    pim_op = pim_op.text
    leave_op = leave_op.text
    time_op = time_op.text
    rec_op = rec_op.text
    info_op = info_op.text
    perf_op = perf_op.text
    dash_op = dash_op.text
    direc_op = direc_op.text
    main_op = main_op.text
    buzz_op = buzz_op.text

    if admin_op == admin:
        print(admin_op)
    if pim_op == pim:
        print(pim_op)
    if leave_op == leave:
        print(leave_op)
    if time_op == time1:
        print(time_op)
    if rec_op == recruitment:
        print(rec_op)
    if info_op == info:
        print(info_op)
    if perf_op == performance:
        print(perf_op)
    if dash_op == dashboard:
        print(dash_op)
    if direc_op == directory:
        print(direc_op)
    if main_op == maintenance:
        print(direc_op)
    if buzz_op == buzz:
        print(buzz_op)
    else:
        print("Menu's are wrong")








#tc_pim_01()
#tc_pim_02()
tc_pim_03()