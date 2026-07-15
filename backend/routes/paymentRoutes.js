const express = require('express');
const router = express.Router();
const Razorpay = require('razorpay');
const crypto = require('crypto');
const { auth } = require('../middleware/auth');

// Initialize Razorpay (with dummy fallbacks to prevent startup crash if keys are missing)
if (!process.env.RAZORPAY_KEY_ID || !process.env.RAZORPAY_KEY_SECRET) {
    console.warn("⚠️ WARNING: RAZORPAY_KEY_ID or RAZORPAY_KEY_SECRET environment variables are missing. Razorpay payments will run in simulation/fallback mode.");
}

const razorpay = new Razorpay({
    key_id: process.env.RAZORPAY_KEY_ID || 'rzp_test_dummy_key_id',
    key_secret: process.env.RAZORPAY_KEY_SECRET || 'dummy_key_secret'
});

// Create Order
router.post('/create-order', auth, async (req, res) => {
    try {
        const { amount, currency = 'INR', receipt } = req.body;

        if (!amount) {
            return res.status(400).json({ error: 'Amount is required' });
        }

        const options = {
            amount: amount * 100, // Razorpay works in paise
            currency,
            receipt: receipt || `receipt_${Date.now()}`,
        };

        const order = await razorpay.orders.create(options);
        
        if (!order) {
            return res.status(500).json({ error: 'Failed to create Razorpay order' });
        }

        res.status(200).json(order);
    } catch (err) {
        console.error('Razorpay Order Error:', err);
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

// Verify Payment
router.post('/verify-payment', auth, async (req, res) => {
    try {
        const { razorpay_order_id, razorpay_payment_id, razorpay_signature } = req.body;

        const sign = razorpay_order_id + "|" + razorpay_payment_id;
        const expectedSign = crypto
            .createHmac("sha256", process.env.RAZORPAY_KEY_SECRET)
            .update(sign.toString())
            .digest("hex");

        if (razorpay_signature === expectedSign) {
            // Payment verified
            return res.status(200).json({ message: "Payment verified successfully", success: true });
        } else {
            return res.status(400).json({ error: "Invalid signature", success: false });
        }
    } catch (err) {
        console.error('Razorpay Verify Error:', err);
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

module.exports = router;
