const router = require('express').Router();
const passport = require('passport');

// auth login
router.get('/login', (req, res) => {
    res.render('login', { user: req.user });
});

// auth logout
router.get('/logout', (req, res) => {
    // handle with passport
    res.send('logging out');
});

// auth with google+
router.get('/google', passport.authenticate('google', {
    scope: ['profile']
}));

// callback route for google to redirect to
// take that URI code that came back & exchange that code with Google for profile information
// goes back to passport-setup
router.get('/google/redirect', passport.authenticate('google'), (req, res) => {
    // now we have access to user
    res.send('you reached the redirect URI' + req.user);
});

module.exports = router;