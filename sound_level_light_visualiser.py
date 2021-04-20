import time
import pyaudio
import RPi.GPIO as GPIO
import math
import numpy
import audioop
import RPi.GPIO as GPIO
import threading

def record_audio(target_time):
    # while we have available time we modulate the LED
    while target_time > time.time():
        raws=stream.read(1024)
        decibel = getDecibels(raws)
        change_LED_brightness_PMW(decibel)

def getDecibels(raws):
    # we apply a rms and then the decibel formula to the raws
    rms = audioop.rms(raws, 2)
    if(rms is not 0):
        return 20 * numpy.log10(rms)
    return 0

def change_LED_brightness_PMW(decibels):
    # we change the led duty cycle value based on the number of decibels
    soft_pwm.ChangeDutyCycle(get_duty_cycle_for_value(decibels))

def get_duty_cycle_for_value(decibel):
    # this function returns the duty cycle value based on the number of decibels
    if(decibel <= 10):
        return 0
    computed_val = (decibel - 10) * (100/70)
    if computed_val > 99:
        return 100
    return computed_val
    
def cleanup():
    # we cleanup the allocated resources
    turn_off_led()
    GPIO.cleanup()        
    stream.stop_stream()
    stream.close()
    p.terminate()

def turn_off_led():
    print("Led turned off..")
    soft_pwm.ChangeDutyCycle(0)
    soft_pwm.stop()
    
def run():
    try:
        seconds = int(input("\n\nEnter the number of seconds for which you want to run the app:"))
        record_audio(seconds + time.time())
    except (Exception, KeyboardInterrupt):
        pass
    cleanup()
    print("Application stopped")


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
soft_pwm = GPIO.PWM(17, 60)
soft_pwm.start(0)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
                channels=2,
                rate=44100,
                input=True,
                frames_per_buffer=1024)

run()
