#!/usr/bin/node
var Odoo = require("odoo-xmlrpc");
const odoo = new Odoo({
  url: "localhost",
  port: "8069",
  db: "odoo_insider",
  username: "admin",
  password: "admin",
});
async function create_chatter_msg(ticket_id, body, author_id) {
  odoo.connect(function (err) {
    if (err) {
      reject(err);
    }

    odoo.execute_kw(
      "helpdesk.ticket",
      "message_post",
      [
        [parseInt(ticket_id)],
        {
          body: body,
          author_id: author_id,
          subtype_xmlid: "mail.mt_comment",
          message_type: "comment",
        },
      ],
      (...args) => {
        console.log(args);
      }
    );
  });
}

create_chatter_msg(1, "Hello", 1);
