import { h } from 'preact';
import { useState } from 'preact/hooks'
import { Link } from 'preact-router/match';
import style from './style.css';
import 'css.gg/icons/css/home.css'
import 'css.gg/icons/css/user.css'
import 'css.gg/icons/css/album.css'
import 'css.gg/icons/css/server.css'
import 'css.gg/icons/css/phone.css'
import 'css.gg/icons/css/menu.css'
import 'css.gg/icons/css/close.css'


const Header = () => {

	const [isMobileActive, setMobileActive] = useState(0);
	const toggleMenu = () => {
		setMobileActive(!isMobileActive);
		document.querySelector('body').classList.toggle('mobile-nav-active')
	}

	return (
		<>
			<button type="button" class="mobile-nav-toggle d-xl-none"
				onClick={toggleMenu}>
				<i class={isMobileActive ? "gg-close" : "gg-menu"}></i>
			</button>
			<header id="header" class="d-flex flex-column justify-content-center">
				<nav id="navbar" class="navbar nav-menu" style={{ display: 'block' }} >
					<ul>
						<li>
							<Link href="/" class="nav-link scrollto" activeClassName='active' onClick={toggleMenu}>
								<i class="gg-home"></i> <span>Home</span>
							</Link>
						</li>
						<li>
							<Link href="/manual/" class="nav-link scrollto" activeClassName='active' onClick={toggleMenu}>
								<i class="gg-user"></i> <span>Manually Control</span>
							</Link>
						</li>
						<li>
							<Link href="/setting/" class="nav-link scrollto" activeClassName='active' onClick={toggleMenu}>
								<i class="gg-album"></i> <span>Sensor Calibration </span>
							</Link>
						</li>
						<li>
							<Link href="/services/" class="nav-link scrollto" activeClassName='active' onClick={toggleMenu}>
								<i class="gg-server"></i> <span>Services</span>
							</Link>
						</li>
						<li>
							<Link href="/contact/" class="nav-link scrollto" activeClassName='active'>
								<i class="gg-phone"></i> <span>Contact</span>
							</Link>
						</li>
					</ul>
				</nav>
			</header>
		</>
	)
}


export default Header;
