import React from 'react';
import { NavLink } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';
import { 
  LayoutDashboard,
  Users,
  Activity,
  Calendar,
  FileText,
  UserPlus,
  Stethoscope,
  BarChart3,
  Settings,
  HelpCircle
} from 'lucide-react';

const Sidebar = () => {
  const { user, isAdmin, isDoctor, isNurse } = useAuth();

  const navigation = [
    {
      name: 'Dashboard',
      href: '/dashboard',
      icon: LayoutDashboard,
      roles: ['admin', 'doctor', 'nurse']
    },
    {
      name: 'Patients',
      href: '/patients',
      icon: Users,
      roles: ['admin', 'doctor', 'nurse']
    },
    {
      name: 'Vitals',
      href: '/vitals',
      icon: Activity,
      roles: ['admin', 'doctor', 'nurse']
    },
    {
      name: 'Appointments',
      href: '/appointments',
      icon: Calendar,
      roles: ['admin', 'doctor', 'nurse']
    },
    {
      name: 'Reports',
      href: '/reports',
      icon: FileText,
      roles: ['admin', 'doctor', 'nurse']
    },
    {
      name: 'Doctors',
      href: '/doctors',
      icon: Stethoscope,
      roles: ['admin']
    },
    {
      name: 'Analytics',
      href: '/analytics',
      icon: BarChart3,
      roles: ['admin', 'doctor']
    },
    {
      name: 'User Management',
      href: '/users',
      icon: UserPlus,
      roles: ['admin']
    }
  ];

  const filteredNavigation = navigation.filter(item => 
    item.roles.includes(user?.role)
  );

  return (
    <aside className="w-64 bg-white shadow-sm border-r border-gray-200 min-h-screen">
      <nav className="px-4 py-6">
        {/* Main Navigation */}
        <div className="space-y-1">
          {filteredNavigation.map((item) => {
            const Icon = item.icon;
            return (
              <NavLink
                key={item.name}
                to={item.href}
                className={({ isActive }) =>
                  `sidebar-link ${isActive ? 'active' : ''}`
                }
              >
                <Icon className="w-5 h-5 mr-3" />
                {item.name}
              </NavLink>
            );
          })}
        </div>

        {/* Bottom Section */}
        <div className="mt-auto pt-6 border-t border-gray-200">
          <div className="space-y-1">
            <NavLink to="/settings" className="sidebar-link">
              <Settings className="w-5 h-5 mr-3" />
              Settings
            </NavLink>
            <NavLink to="/help" className="sidebar-link">
              <HelpCircle className="w-5 h-5 mr-3" />
              Help & Support
            </NavLink>
          </div>
        </div>
      </nav>
    </aside>
  );
};

export default Sidebar;
