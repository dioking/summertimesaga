screen _exception_actions(traceback_fn, tt, *args):
    textbutton _('Open'):
        action _EditFile(traceback_fn)
        hovered tt.action(_('Opens the traceback.txt file in a text editor.'))

    textbutton _('Copy'):
        action _CopyFile(traceback_fn, '```\n{}```\n')
        hovered tt.action(_('Copies the traceback.txt file to the clipboard as Markdown for Discord.'))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
