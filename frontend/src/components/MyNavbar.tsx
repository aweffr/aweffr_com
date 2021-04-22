import React, {useState} from 'react';
import {Collapse, Nav, Navbar, NavbarBrand, NavbarToggler, NavItem, NavLink} from 'reactstrap';

const MyNavLink = ({href, children}: {href: string, children: string}) => {
  const isActive = window.location.pathname.includes(href);
  return (
    <NavLink className={"my-nav-link " + (isActive ? "nav-active" : "nav-inactive")} href={href}>{children}</NavLink>
  )
};

const MyNavbar: React.FC = () => {
  const [isOpen, setIsOpen] = useState(false);
  const toggle = () => setIsOpen(!isOpen);

  return (
    <div>
      <Navbar color="light" light expand="md">
        <NavbarBrand href="/">aweffr的小站</NavbarBrand>
        <NavbarToggler onClick={toggle}/>
        <Collapse isOpen={isOpen} navbar>
          <Nav className="mr-auto" navbar>
            <NavItem>
              <MyNavLink href="/article/">随笔</MyNavLink>
            </NavItem>
            <NavItem>
              <MyNavLink href="/study/">学习</MyNavLink>
            </NavItem>
            <NavItem>
              <MyNavLink href="/archive/">收藏</MyNavLink>
            </NavItem>
            <NavItem>
              <MyNavLink href="/tweet/">碎碎念</MyNavLink>
            </NavItem>
          </Nav>
          <Nav navbar>
            <NavItem>
              <MyNavLink href="/tool/">工具箱</MyNavLink>
            </NavItem>
          </Nav>
        </Collapse>
      </Navbar>
    </div>
  );
}

export default MyNavbar;
