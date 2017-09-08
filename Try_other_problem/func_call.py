import cmd

class example(cmd.Cmd):
    prompt  = '<input> '

    def do_func1(self, arg):
        print 'func1 - call'

    def do_func2(self, arg):
        print 'func2 - call'

    def do_func3(self, arg):
        print 'func3 - call'

example().cmdloop()
