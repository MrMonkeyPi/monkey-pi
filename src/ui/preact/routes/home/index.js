import { h } from 'preact';
import style from './style.css';

const Home = () => (
	<section id="home" class="d-flex flex-column justify-content-center">
		<div class="container" data-aos="zoom-in" data-aos-delay="100">
			<h1>Mr. Monkey Pi</h1>
			<p>I'm <span class="typed" data-typed-items="Developer, Freelancer"></span></p>

		</div>
	</section>
);

export default Home;
