const express = require('express');
const mongoose = require('mongoose');
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(express.json());

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/taskmanager', { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('MongoDB connected'))
  .catch(err => console.error(err));

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
Define Mongoose Schema:

Created a new file Task.js to define the Mongoose schema for tasks.
javascript
Copy code
const mongoose = require('mongoose');

const taskSchema = new mongoose.Schema({
  title: { type: String, required: true },
  completed: { type: Boolean, default: false },
});

module.exports = mongoose.model('Task', taskSchema);
Implement CRUD Operations:

In server.js, added routes to create, read, update, and delete tasks using the Mongoose model.
javascript
Copy code
const Task = require('./Task');

// Create a new task
app.post('/tasks', async (req, res) => {
  const task = new Task(req.body);
  try {
    await task.save();
    res.status(201).send(task);
  } catch (err) {
    res.status(400).send(err);
  }
});

// Get all tasks
app.get('/tasks', async (req, res) => {
  const tasks = await Task.find();
  res.send(tasks);
});

// Update a task
app.patch('/tasks/:id', async (req, res) => {
  try {
    const task = await Task.findByIdAndUpdate(req.params.id, req.body, { new: true });
    res.send(task);
  } catch (err) {
    res.status(400).send(err);
  }
});

// Delete a task
app.delete('/tasks/:id', async (req, res) => {
  try {
    await Task.findByIdAndDelete(req.params.id);
    res.sendStatus(204);
  } catch (err) {
    res.status(500).send(err);
  }
});
Test the API:

Used Postman to test the API endpoints for creating, retrieving, updating, and deleting tasks.
Challenges Faced
Mongoose Connection Issues:
Initially faced challenges connecting to MongoDB. After some troubleshooting, I realized I needed to ensure that the MongoDB service was running locally and that I was using the correct connection string.

Schema Validation:
Encountered errors while trying to save tasks due to validation issues in the schema. I had to ensure that the required fields were being sent in the requests.

Async/Await Handling:
Using async/await for database operations was a bit tricky at first, especially with error handling. I learned to use try-catch blocks to manage errors effectively.

Testing API Endpoints:
Initially, I didn’t test the endpoints thoroughly, which led to some unexpected behavior when trying to update or delete tasks. I needed to add more comprehensive error checks and responses.

Project Repository
Here’s a link to the project repository: GitHub Repository