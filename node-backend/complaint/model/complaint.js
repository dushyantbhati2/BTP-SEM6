const mongoose = require("mongoose");

const complaintSchema = new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, required: true },
    complaint: { type: String, required: true },
    createdAt: { type: Date, default: Date.now },
});

const Complaint = mongoose.model("Complaint", complaintSchema);
module.exports = Complaint;