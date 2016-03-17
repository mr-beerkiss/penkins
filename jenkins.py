import time, sys

from jenkinsapi.jenkins import Jenkins

def get_dummy_build_info(jenkins, job_name):
    job = jenkins.get_job(job_name)
    build = job.get_last_build()
    # print(dir(build))
    if build == None:
        print 'Cannot retrieve build information'
    else:
        status = build.get_status()
        if status == 'SUCCESS':
            print 'Success'
        elif status == 'ABORTED':
            print 'Aborted'
        elif status == 'FAILURE':
            print 'Failure'
        elif status == None and build.is_running():
            print 'Running'
        else:
            print 'Unknown status'

if __name__ == '__main__':
    if len(sys.argv) != 7 :
        print 'Error. Usage: '
        print ' python jenkins.py -u <username> -t <token> -j <job_name>'
        sys.exit(2)
    else:
        username = str(sys.argv[2])
        token = str(sys.argv[4])
        job_name = str(sys.argv[6])

    jenkins_url = 'http://ci.boxtop.photobox.com'
    jenkins = Jenkins(jenkins_url, username = username, password = token)

    while 1==1:
        get_dummy_build_info(jenkins, job_name)
        time.sleep(5)
