import React, {useState} from 'react';
import {Collapse, Nav, Navbar, NavbarBrand, NavbarToggler, NavItem, NavLink} from 'reactstrap';

const MyNavLink = ({href, children}: {href: string, children: string}) => {

  const isActive = window.location.pathname.includes(href);

  return (
    <NavLink className="my-nav-link" href={href} active={isActive}>{children}</NavLink>
  )
};

const MyNavbar = () => {
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
              <MyNavLink href="/archives/">归档</MyNavLink>
            </NavItem>
            <NavItem>
              <MyNavLink href="/todo/">todo清单</MyNavLink>
            </NavItem>
            <NavItem>
              <MyNavLink href="/tweets/">碎碎念</MyNavLink>
            </NavItem>
          </Nav>
          <Nav navbar>
            <NavItem>
              <MyNavLink href="/tools/">工具箱</MyNavLink>
            </NavItem>
          </Nav>
        </Collapse>
      </Navbar>
    </div>
  );
}

export default MyNavbar;
