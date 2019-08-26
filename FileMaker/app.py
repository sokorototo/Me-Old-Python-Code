print('First let us store something')
file_name=input('What file do you want to create?\n(Put within braces): ')
the_file=open(file_name,'w')
while True:
        i=0
        while i<=3:
                the_file.write(str(input('Add some thing: ')+"\n"))
                i+=1
        test=input('Continue?(y/n): ').lower()
        if test=='n':
                break
the_file.close()