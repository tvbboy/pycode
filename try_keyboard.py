try:
    inp = input("Press Ctrl+C or Interrupt the Kernel:")
except KeyboardInterrupt:
    print('Caught KeyboardInterrupt')
else:
    print('No exception occurred')
