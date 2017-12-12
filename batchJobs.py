from apscheduler.schedulers.blocking import BlockingScheduler
import fetchExchangeRates
sched = BlockingScheduler()

@sched.scheduled_job('cron', hour=21, minute=27)
def scheduled_job():
    fetchExchangeRates.fetchExchangeRates()

sched.start()
