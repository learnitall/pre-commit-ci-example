#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bad python file that will be autofixed."""


def main():
    my_string = "this is my really really really really really really really really really really really really really really really really really really really really really really long string."

    my_set = {1, 2, 3, 4}

    def this_is_a_function_with_lots_of_args(
        arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15
    ):
        print(
            "I ran this really long function with a lot of args: {} {} {} {} {} {}".format(
                arg1, arg2, arg3, arg4, arg5
            )
        )

    print("Hey check out this string: %s" % my_string)


main()
