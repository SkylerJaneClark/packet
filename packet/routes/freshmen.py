"""
Routes available to freshmen only
"""

from flask import redirect, render_template, request, url_for

from packet import app, db
from packet.models import Packet
from packet.utils import before_request, packet_auth


@app.route("/")
@packet_auth
@before_request
def index(info=None):
    most_recent_packet = Packet.query.filter_by(freshman_username=info['uid']).order_by(Packet.id.desc()).first()

    if most_recent_packet is not None:
        return redirect(url_for("freshman_packet", packet_id=most_recent_packet.id), 302)
    else:
        return redirect(url_for("packets"), 302)
