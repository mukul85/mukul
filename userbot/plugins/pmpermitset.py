import heroku3
import asyncio
import os
import requests
import math
from userbot.utils import register
from userbot.utils import admin_cmd
Heroku = heroku3.from_key(Var.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
@register(outgoing=True, pattern=r"^\.(pmpermitset) var(?: |$)(.*)(?: |$)([\s\S]*)")
async def variable(var):
    if Var.HEROKU_APP_NAME is not None:
        app = Heroku.app(Var.HEROKU_APP_NAME)
    else:
        return await var.edit("`[HEROKU]:"
                              "\nPlease setup your` **HEROKU_APP_NAME**")
    exe = var.pattern_match.group(1)
    if exe == "pmpermitset":
        await var.edit("`Setting pmpermit...`")
        variable = PMPERMIT_PIC
        if not variable:
            return await var.edit(">`.set var <value>`")
        value = var.pattern_match.group(2)
        if not value:
            variable = variable.split()[0]
            try:
                value = var.pattern_match.group(2).split()[1]
            except IndexError:
                return await var.edit(">`.set var <ConfigVars-name> <value>`")
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await var.edit(f"**{variable}**  `successfully changed to`  ->  **{value}**")
        else:
            await var.edit(f"**{variable}**  `successfully added with value`  ->  **{value}**")
        heroku_var[variable] = value
