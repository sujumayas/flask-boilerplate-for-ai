// frontend/src/components/__tests__/UserList.test.jsx
import { render, screen, waitFor } from '@testing-library/react';
import UserList from '../UserList';
import { getUsers } from '../../services/api';

// Mock the API service
jest.mock('../../services/api');

describe('UserList Component', () => {
  test('renders users fetched from API', async () => {
    // Arrange: Mock API response
    getUsers.mockResolvedValue({
      data: [
        { id: 1, username: 'testuser1', email: 'test1@example.com' },
        { id: 2, username: 'testuser2', email: 'test2@example.com' },
      ],
    });

    // Act: Render component
    render(<UserList />);

    // Assert: Check if users are displayed
    await waitFor(() => {
      expect(screen.getByText('testuser1 (test1@example.com)')).toBeInTheDocument();
      expect(screen.getByText('testuser2 (test2@example.com)')).toBeInTheDocument();
    });
  });

  test('handles API errors gracefully', async () => {
    // Arrange: Mock API to reject
    getUsers.mockRejectedValue(new Error('API Error'));

    // Spy on console.error
    const consoleSpy = jest.spyOn(console, 'error').mockImplementation(() => {});

    // Act: Render component
    render(<UserList />);

    // Assert: Ensure error was logged
    await waitFor(() => {
      expect(consoleSpy).toHaveBeenCalledWith('Failed to fetch users:', expect.any(Error));
    });

    consoleSpy.mockRestore();
  });
});
