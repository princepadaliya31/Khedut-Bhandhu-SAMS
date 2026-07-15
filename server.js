const path = require('path');

// Target directory and file
const targetDir = path.join(__dirname, 'backend');
const targetFile = path.join(targetDir, 'server.js');

console.log('🚀 Redirecting to actual server in:', targetDir);

try {
    // Change Current Working Directory so .env and other relative paths work
    process.chdir(targetDir);

    // Require the actual server file
    require(targetFile);
} catch (err) {
    console.error("❌ Failed to start server:", err.message);
    console.error("Ensure 'backend' folder exists and contains 'server.js'.");
}
