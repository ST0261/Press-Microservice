The function of this module is only send emails

# Contract

## Send-Email

### Recive - Json
{
    emails:[
        {
            "subject": " <Subject>",
            "content": " <Content> "
        }
    ]
}

### Retuns - Json

{
    "status": "Done" | "err",
    "Description": "Ok" | "err description"
}
