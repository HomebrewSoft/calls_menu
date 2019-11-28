
Calls Menu
==========

Server action
-------------

```python
Message = env['mail.message']
activities = env['mail.activity'].search([('res_model', '=', 'res.partner'), ('activity_type_id.name', '=', 'Llamada')])

for activity in activities:
    a = Message.with_env(env(user=activity.user_id.id)).create({
        'message_type': 'comment',
        'subject': activity.summary,
        'date': min(activity.write_date, activity.create_date),
        'body': activity.note,
        'model': activity.res_model,
        'res_id': activity.res_id,
    })

activities.unlink()
```
