import { h } from 'preact';
import { Router } from 'preact-router';

import Header from './header';

import Home from '../routes/home';
import Manual from '../routes/manual';
import Setting from '../routes/setting';

const App = () => (
	<div id="app">
		<Header />
		<Router>
			<Home path="/" />
			<Manual path="/manual" />
			<Setting path="/setting"/>
		</Router>
	</div>
)

export default App;
