import { render } from 'preact';
import './style/index.css';
import App from './components/app';


render(App(), document.getElementById('root'));

fetch(`/api/status/init`).catch(x=> alert('failed to init hardware'))