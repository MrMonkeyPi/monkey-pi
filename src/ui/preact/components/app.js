import { h } from 'preact';
import { Router } from 'preact-router';

import Header from './header';

import Home from '../routes/home';
import Manual from '../routes/manual';

const App = () => (
	<div id="app">
		<Header />
		<Router>
			<Home path="/" />
			<Manual path="/manual" />
		</Router>
	</div>
)

export default App;
